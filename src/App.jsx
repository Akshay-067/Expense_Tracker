import { useState } from "react";
import AuthForm from "./AuthForm.jsx";
import Expenses from "./Expenses.jsx";

export default function App() {
  const [token, setToken] = useState(localStorage.getItem("token"));

  return (
    <div>
      <AuthForm setToken={setToken} />
      {token && <Expenses token={token} />}
    </div>
  );
}