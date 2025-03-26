document.addEventListener("DOMContentLoaded", function () {
    fetch('/api/students/')  // Replace with the correct URL of your API
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('student-data');
            data.forEach(student => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${student.ReqNo}</td>
                    <td>${student.Name}</td>
                    <td>${student.branch}</td>
                    <td>${student.year}</td>
                    <td>${student.address}</td>
                    <td>${student.city}</td>
                    <td>${student.state}</td>
                    <td>${student.country}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});
