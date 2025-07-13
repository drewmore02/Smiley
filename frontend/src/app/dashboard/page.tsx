import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export default function DashboardPage() {
  return (
    <main className="p-8">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <Card>
        <CardHeader>
          <CardTitle>Welcome, Drew!</CardTitle>
        </CardHeader>
        <CardContent>
          <p>This is your new scouting camp management dashboard.</p>
          <Button className="mt-4">View Programs</Button>
        </CardContent>
      </Card>
    </main>
  );
}