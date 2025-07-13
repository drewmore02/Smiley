export interface Program {
  id: number;
  name: string;
  description: string;
  campId: number;
  startDate: string | null;
  endDate: string | null;
}