import { BrowserRouter, Routes, Route } from "react-router-dom";
import Admin from "../modules/admin/admin";
import Dashboard from "../modules/dashboard/dashboard";

const AppRoutes = () => (
  <BrowserRouter>
    <Routes>
      <Route path="/admin" element={<Admin />} />
      <Route path="/dashboard" element={<Dashboard />} />
    </Routes>
  </BrowserRouter>
);

export default AppRoutes;
