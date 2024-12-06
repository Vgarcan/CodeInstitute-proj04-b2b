document.addEventListener("DOMContentLoaded", function() {
    const userRole = userConfig.userRole; // Pasado desde Django

    // Identifica los elementos canvas según el rol
    const buyerChartCanvas = document.getElementById("buyerSpendingChart");
    const supplierChartCanvas = document.getElementById("supplierSalesChart");

    // Función para inicializar gráficos
    function initChart(canvas, data, labels, labelName) {
        new Chart(canvas, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: labelName,
                    data: data,
                    backgroundColor: 'rgba(54, 162, 235, 0.5)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Función para obtener datos de la API
    function fetchChartData(role, canvas, labelName) {
        fetch(`/orders/api/chart-data/${role}/`)
            .then(response => response.json())
            .then(data => {
                initChart(canvas, data.data, data.labels, labelName);
            })
            .catch(error => console.error("Error fetching chart data:", error));
    }

    // Renderiza el gráfico para compradores si es necesario
    if (userRole === "BUY" && buyerChartCanvas) {
        fetchChartData("buyer", buyerChartCanvas, "Total Spent (£)");
    }

    // Renderiza el gráfico para proveedores si es necesario
    if (userRole === "SUP" && supplierChartCanvas) {
        fetchChartData("supplier", supplierChartCanvas, "Total Earned (£)");
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const userRole = window.userConfig.userRole;

    const transactionCanvas = document.getElementById("transactionStatusChart");

    if (transactionCanvas) {
        // Fetch data for the circular chart
        fetch(`/orders/api/transaction-status/`)
            .then(response => response.json())
            .then(data => {
                new Chart(transactionCanvas, {
                    type: "doughnut", // Doughnut chart type
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: "Transaction Status",
                            data: data.data,
                            backgroundColor: [
                                "rgba(255, 99, 132, 0.6)", // Pending
                                "rgba(54, 162, 235, 0.6)", // Completed
                                "rgba(255, 206, 86, 0.6)", // Cancelled
                                "rgba(75, 192, 192, 0.6)", // Processing
                                "rgba(153, 102, 255, 0.6)", // Delivered
                                "rgba(255, 159, 64, 0.6)", // Shipped
                            ],
                            borderColor: [
                                "rgba(255, 99, 132, 1)",
                                "rgba(54, 162, 235, 1)",
                                "rgba(255, 206, 86, 1)",
                                "rgba(75, 192, 192, 1)",
                                "rgba(153, 102, 255, 1)",
                                "rgba(255, 159, 64, 1)",
                            ],
                            borderWidth: 1,
                        }],
                    },
                    options: {
                        responsive: true,
                        plugins: {
                            legend: {
                                position: "top",
                            },
                        },
                    },
                });
            })
            .catch(error => console.error("Error fetching transaction status data:", error));
    }
});