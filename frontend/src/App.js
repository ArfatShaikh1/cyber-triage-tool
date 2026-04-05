import React, { useState } from 'react';

const App = () => {
    const [caseInput, setCaseInput] = useState('');
    const [file, setFile] = useState(null);

    const handleCaseInputChange = (e) => {
        setCaseInput(e.target.value);
    };

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleAnalysis = () => {
        // Placeholder for analysis functionality
        alert('Analysis in progress...');
    };

    const handleReportGeneration = () => {
        // Placeholder for report generation functionality
        alert('Report generated!');
    };

    return (
        <div>
            <h1>Cyber Triage Tool</h1>
            <div>
                <label htmlFor="caseInput">Case Input:</label>
                <input 
                    type="text" 
                    id="caseInput" 
                    value={caseInput} 
                    onChange={handleCaseInputChange} 
                />
            </div>
            <div>
                <label htmlFor="fileUpload">Upload File:</label>
                <input 
                    type="file" 
                    id="fileUpload" 
                    onChange={handleFileChange} 
                />
            </div>
            <button onClick={handleAnalysis}>Analyze</button>
            <button onClick={handleReportGeneration}>Generate Report</button>
        </div>
    );
};

export default App;