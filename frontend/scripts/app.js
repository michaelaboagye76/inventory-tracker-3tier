const API_BASE = "http://localhost:5000"; // replace later with your Beanstalk URL
const tableBody = document.querySelector("#inventoryTable tbody");
const form = document.getElementById("itemForm");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  
  const name = document.getElementById("itemName").value.trim();
  const quantity = document.getElementById("itemQuantity").value;
  const branch = document.getElementById("branch").value.trim();

  const response = await fetch(`${API_BASE}/inventory`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ name, quantity, branch })
  });

  if (response.ok) {
    await fetchInventory();
    form.reset();
  } else {
    alert("Failed to add item");
  }
});

async function fetchInventory() {
  const response = await fetch(`${API_BASE}/inventory`);
  const data = await response.json();
  renderTable(data);
}

function renderTable(data) {
  tableBody.innerHTML = "";
  data.forEach(item => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${item.id}</td>
      <td>${item.name}</td>
      <td>${item.quantity}</td>
      <td>${item.branch}</td>
      <td>
        <button onclick="deleteItem(${item.id})">Delete</button>
      </td>
    `;
    tableBody.appendChild(row);
  });
}

async function deleteItem(id) {
  const response = await fetch(`${API_BASE}/inventory/${id}`, {
    method: "DELETE"
  });
  if (response.ok) {
    await fetchInventory();
  } else {
    alert("Failed to delete item");
  }
}

// Load data when the page opens
window.onload = fetchInventory;
