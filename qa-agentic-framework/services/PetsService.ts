import type { APIRequestContext, APIResponse } from "@playwright/test";

export interface PetPayload {
  name: string;
  type: string;
  age: number;
}

export interface Pet extends PetPayload {
  id: number;
}

export class PetsService {
  constructor(
    private readonly request: APIRequestContext,
    private readonly baseUrl: string,
  ) {}

  getPets(): Promise<APIResponse> {
    return this.request.get(`${this.baseUrl}/pets`);
  }

  createPet(payload: Partial<PetPayload>): Promise<APIResponse> {
    return this.request.post(`${this.baseUrl}/pets`, { data: payload });
  }

  getPet(id: number): Promise<APIResponse> {
    return this.request.get(`${this.baseUrl}/pets/${id}`);
  }

  updatePet(id: number, payload: PetPayload): Promise<APIResponse> {
    return this.request.put(`${this.baseUrl}/pets/${id}`, { data: payload });
  }

  patchPet(id: number, payload: Partial<PetPayload>): Promise<APIResponse> {
    return this.request.patch(`${this.baseUrl}/pets/${id}`, { data: payload });
  }

  deletePet(id: number): Promise<APIResponse> {
    return this.request.delete(`${this.baseUrl}/pets/${id}`);
  }
}
