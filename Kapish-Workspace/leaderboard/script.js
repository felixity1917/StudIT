// Simulate real-time data (you can replace this with actual API calls or database integration)
const leaderboardData = [
    { rank: 1, name: 'John Doe', branch: 'Computer Science', year: '3rd', score: 95 },
    { rank: 2, name: 'Jane Smith', branch: 'Mechanical Engineering', year: '2nd', score: 92 },
    { rank: 3, name: 'Alex Brown', branch: 'Electronics', year: '1st', score: 88 },
    // More data can be added here
];

function loadLeaderboard() {
    const leaderboardBody = document.getElementById('leaderboard-body');

    leaderboardData.forEach(student => {
        const row = document.createElement('tr');
        
        row.innerHTML = `
            <td>${student.rank}</td>
            <td>${student.name}</td>
            <td>${student.branch}</td>
            <td>${student.year}</td>
            <td>${student.score}</td>
        `;
        
        leaderboardBody.appendChild(row);
    });
}

// Load data on page load
window.onload = loadLeaderboard;
