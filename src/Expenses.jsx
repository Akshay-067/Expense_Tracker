import { useState } from "react";

const API = "http://127.0.0.1:8000";

export default function Expenses({ token }) {
  const [expenses, setExpenses] = useState([]);
  const [msg, setMsg] = useState("");

  async function getExpenses() {
    const res = await fetch(`${API}/expenses?user_id=1`, {
      headers: { token: token },
    });
    const data = await res.json();
    if (res.ok) setExpenses(data);
    else setMsg(data.detail);
  }

  return (
    <div>
      <button onClick={getExpenses}>Get Expenses</button>
      <p>{msg}</p>
      {expenses.map((e) => (
        <p key={e.id}>{e.title} - ₹{e.amount} ({e.category})</p>
      ))}
    </div>
  );
}