import { expect, test, type APIResponse } from "@playwright/test";
import {
  PetsService,
  type Pet,
  type PetPayload,
} from "../../services/PetsService.js";

interface ApiResponse<T> {
  status: string;
  message: string;
  data: T;
}

const baseUrl =
  process.env.PETS_API_BASE_URL ?? "https://pets-demo.onrender.com";
const slaMs = 30000;

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function isPet(value: unknown): value is Pet {
  return (
    isRecord(value) &&
    typeof value.id === "number" &&
    typeof value.name === "string" &&
    typeof value.type === "string" &&
    typeof value.age === "number"
  );
}

function isPetResponse(value: unknown): value is ApiResponse<Pet> {
  return (
    isRecord(value) &&
    value.status === "success" &&
    typeof value.message === "string" &&
    isPet(value.data)
  );
}

function isPetsResponse(value: unknown): value is ApiResponse<Pet[]> {
  return (
    isRecord(value) &&
    value.status === "success" &&
    typeof value.message === "string" &&
    Array.isArray(value.data) &&
    value.data.every(isPet)
  );
}

function isErrorResponse(value: unknown): value is ApiResponse<null> {
  return (
    isRecord(value) &&
    value.status === "error" &&
    typeof value.message === "string" &&
    value.data === null
  );
}

async function measureRequest(action: () => Promise<APIResponse>) {
  const startedAt = Date.now();
  const response = await action();
  return { response, elapsedMs: Date.now() - startedAt };
}

function expectJson(response: APIResponse) {
  expect(response.headers()["content-type"]).toMatch(/application\/json/i);
}

function expectSla(elapsedMs: number) {
  expect(elapsedMs).toBeLessThan(slaMs);
}

function createPayload(): PetPayload {
  return {
    name: `Mimi-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
    type: "Gato",
    age: 2,
  };
}

async function createTrackedPet(
  petsService: PetsService,
  createdPetIds: number[],
): Promise<Pet> {
  const payload = createPayload();
  const { response, elapsedMs } = await measureRequest(() =>
    petsService.createPet(payload),
  );

  expect([200, 201]).toContain(response.status());
  expectJson(response);
  expectSla(elapsedMs);

  const body: unknown = await response.json();
  if (
    isRecord(body) &&
    isRecord(body.data) &&
    typeof body.data.id === "number"
  ) {
    createdPetIds.push(body.data.id);
  }

  expect(isPetResponse(body)).toBe(true);
  if (!isPetResponse(body)) {
    throw new Error("Pets endpoint returned an invalid create response");
  }

  expect(body.data.name).toBe(payload.name);
  expect(body.data.type).toBe(payload.type);
  expect(body.data.age).toBe(payload.age);
  return body.data;
}

async function expectErrorResponse(response: APIResponse) {
  expectJson(response);
  const body: unknown = await response.json();
  expect(isErrorResponse(body)).toBe(true);
}

test.describe("GET /pets", () => {
  test("retrieves the pets list with the expected schema", async ({
    request,
  }) => {
    const petsService = new PetsService(request, baseUrl);
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.getPets(),
    );

    expect(response.status()).toBe(200);
    expectJson(response);
    expectSla(elapsedMs);

    const body: unknown = await response.json();
    expect(isPetsResponse(body)).toBe(true);
  });
});

test.describe("POST /pets", () => {
  let petsService: PetsService;
  let createdPetIds: number[];

  test.beforeEach(({ request }) => {
    petsService = new PetsService(request, baseUrl);
    createdPetIds = [];
  });

  test.afterEach(async () => {
    for (const id of createdPetIds) {
      const { response, elapsedMs } = await measureRequest(() =>
        petsService.deletePet(id),
      );
      expect([204, 404]).toContain(response.status());
      expectSla(elapsedMs);
    }
  });

  test("creates a valid pet", async () => {
    await createTrackedPet(petsService, createdPetIds);
  });

  test("rejects an empty payload", async () => {
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.createPet({}),
    );

    expect(response.status()).toBe(400);
    expectJson(response);
    expectSla(elapsedMs);
    await expectErrorResponse(response);
  });

  test("rejects a payload without the name field", async () => {
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.createPet({ type: "Gato", age: 2 }),
    );

    expect(response.status()).toBe(400);
    expectJson(response);
    expectSla(elapsedMs);
    await expectErrorResponse(response);
  });
});

test.describe("GET, PUT, PATCH, and DELETE /pets/:id", () => {
  let petsService: PetsService;
  let createdPetIds: number[];
  let existingPet: Pet;

  test.beforeEach(async ({ request }) => {
    petsService = new PetsService(request, baseUrl);
    createdPetIds = [];
    existingPet = await createTrackedPet(petsService, createdPetIds);
  });

  test.afterEach(async () => {
    for (const id of createdPetIds) {
      const { response, elapsedMs } = await measureRequest(() =>
        petsService.deletePet(id),
      );
      expect([204, 404]).toContain(response.status());
      expectSla(elapsedMs);
    }
  });

  test("retrieves an existing pet by ID", async () => {
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.getPet(existingPet.id),
    );

    expect(response.status()).toBe(200);
    expectJson(response);
    expectSla(elapsedMs);

    const body: unknown = await response.json();
    expect(isPetResponse(body)).toBe(true);
    if (!isPetResponse(body)) {
      throw new Error("Pets endpoint returned an invalid pet response");
    }
    expect(body.data).toEqual(existingPet);
  });

  test("returns 404 for a nonexistent pet ID", async () => {
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.getPet(99999999),
    );

    expect(response.status()).toBe(404);
    expectSla(elapsedMs);
    await expectErrorResponse(response);
  });

  test("updates an existing pet with PUT", async () => {
    const payload: PetPayload = {
      name: `${existingPet.name}-Put`,
      type: "Perro",
      age: 3,
    };
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.updatePet(existingPet.id, payload),
    );

    expect(response.status()).toBe(200);
    expectJson(response);
    expectSla(elapsedMs);

    const body: unknown = await response.json();
    expect(isPetResponse(body)).toBe(true);
    if (!isPetResponse(body)) {
      throw new Error("Pets endpoint returned an invalid PUT response");
    }
    expect(body.data).toEqual({ id: existingPet.id, ...payload });
  });

  test("updates selected fields with PATCH", async () => {
    const payload: Partial<PetPayload> = { age: 4 };
    const { response, elapsedMs } = await measureRequest(() =>
      petsService.patchPet(existingPet.id, payload),
    );

    expect(response.status()).toBe(200);
    expectJson(response);
    expectSla(elapsedMs);

    const body: unknown = await response.json();
    expect(isPetResponse(body)).toBe(true);
    if (!isPetResponse(body)) {
      throw new Error("Pets endpoint returned an invalid PATCH response");
    }
    expect(body.data).toEqual({ ...existingPet, ...payload });
  });

  test("deletes a pet and returns 404 on a subsequent GET", async () => {
    const { response: deleteResponse, elapsedMs: deleteElapsedMs } =
      await measureRequest(() => petsService.deletePet(existingPet.id));

    expect(deleteResponse.status()).toBe(204);
    expectSla(deleteElapsedMs);

    const { response: getResponse, elapsedMs: getElapsedMs } =
      await measureRequest(() => petsService.getPet(existingPet.id));

    expect(getResponse.status()).toBe(404);
    expectSla(getElapsedMs);
    await expectErrorResponse(getResponse);
  });
});
