document.getElementById('research-trigger').addEventListener('submit', function(event) {
    event.preventDefault();
    const reportContainer = document.getElementById('report-container');
    reportContainer.innerHTML = '<p>Researching... Please wait.</p>';

    fetch('http://127.0.0.1:5001/api/research', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        // In a real app, you might send the prompt value
        // body: JSON.stringify({ prompt: document.getElementById('prompt').value })
    })
    .then(response => response.json())
    .then(data => {
        renderReport(data);
    })
    .catch(error => {
        console.error('Error fetching research data:', error);
        reportContainer.innerHTML = '<p>An error occurred. Please check the console and ensure the backend server is running.</p>';
    });
});

function renderReport(data) {
    const reportContainer = document.getElementById('report-container');
    reportContainer.innerHTML = `
        <div class="report-header">
            <h2>${data.reportTitle}</h2>
            <p><strong>Week of:</strong> ${data.weekOf}</p>
        </div>

        <div class="report-section" id="summary">
            <h3>Executive Summary</h3>
            <p>${data.executiveSummary}</p>
        </div>

        <div class="report-section" id="opportunities">
            <h3>Validated Opportunities</h3>
            ${data.validatedOpportunities.map(opp => `
                <div class="opportunity">
                    <h4>${opp.productName} - $${opp.mrr.toLocaleString()} MRR</h4>
                    <p>${opp.description}</p>
                    <p><span class="label">Revenue:</span> ${opp.revenue.metrics} (<a href="${opp.revenue.sourceLink}" target="_blank">Source</a>)</p>
                    <p><span class="label">Marketing:</span> ${opp.marketing}</p>
                    <p><span class="label">Tech/Team:</span> ${opp.techTeam}</p>
                    <p><span class="label">Why it works:</span> ${opp.whyItWorks}</p>
                </div>
            `).join('')}
        </div>

        <div class="report-section" id="patterns">
            <h3>Emerging Patterns</h3>
            <ul>
                ${data.emergingPatterns.map(pattern => `<li>${pattern}</li>`).join('')}
            </ul>
        </div>

        <div class="report-section" id="near-misses">
            <h3>Near Misses</h3>
            <p>${data.nearMisses.join(', ')}</p>
        </div>

        <div class="report-section" id="red-flags">
            <h3>Red Flags Observed</h3>
             <p>${data.redFlagsObserved.join(', ')}</p>
        </div>

        <div class="report-section" id="deep-dives">
            <h3>Recommended Deep Dives</h3>
            <ul>
                ${data.deepDives.map(dive => `<li>${dive}</li>`).join('')}
            </ul>
        </div>

        <div class="report-section" id="market-intel">
            <h3>Market Intelligence</h3>
            <p><span class="label">Trending Hashtags:</span> ${data.marketIntelligence.trendingHashtags.join(', ')}</p>
            <p><span class="label">Active Communities:</span> ${data.marketIntelligence.activeCommunities.join(', ')}</p>
            <p><span class="label">Key Voices to Follow:</span> ${data.marketIntelligence.keyVoices.join(', ')}</p>
        </div>
    `;
}