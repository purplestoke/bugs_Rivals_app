async function connectWallet() {
    if (!window.ethereum) {
        alert("MetaMask is not installed. Please install it to continue.");
        return;
    }

    const web3 = new Web3(window.ethereum);

    try {
        // Request user wallet access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const account = accounts[0];

        // Fetch a nonce from Flask (prevents replay attacks)
        const response = await fetch('/get_nonce', {
            method: 'GET',
            credentials: 'include' // ✅ Fix: Ensures Flask sessions work
        });

        const data = await response.json();
        const message = data.nonce;

        // User signs the message
        const signature = await web3.eth.personal.sign(message, account);

        // Send the signed message to backend for verification
        const verifyResponse = await fetch('/verify_wallet', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            credentials: 'include', // ✅ Fix: Ensures Flask recognizes the session
            body: JSON.stringify({ account, signature, message })
        });

        const verifyData = await verifyResponse.json();

        if (verifyData.success) {
            document.getElementById("login-button").innerText = "Logged in";
            localStorage.setItem("wallet", account); // ✅ Store wallet for session persistence
        } else {
            alert("Login failed: " + verifyData.error);
        }
    } catch (error) {
        console.error("Error connecting wallet:", error);
        alert("Error connecting wallet: " + error.message);
    }
}

// Check if user is already logged in
document.addEventListener("DOMContentLoaded", () => {
    const wallet = localStorage.getItem("wallet");
    if (wallet) {
        document.getElementById("login-button").innerText = "Logged in";
    }
});
