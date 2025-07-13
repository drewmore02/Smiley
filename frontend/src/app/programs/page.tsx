import { Card, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Program } from "@/models/program";

async function getPrograms(): Promise<Program[]> {
  // This fetch runs on the server!
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/programs/`, {
    // Use 'no-cache' during development to always get fresh data
    cache: "no-cache",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch programs");
  }

  return res.json();
}

export default async function ProgramsPage() {
  const programs = await getPrograms();

  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold mb-6">Summer Camp Programs</h1>
      <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
        {programs.map((program) => (
          <Card key={program.id}>
            <CardHeader>
              <CardTitle>{program.name}</CardTitle>
              <CardDescription>{program.description}</CardDescription>
            </CardHeader>
          </Card>
        ))}
      </div>
    </main>
  );
}