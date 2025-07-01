<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔐 Secure Auth System with PyQt5</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
        }
        .features-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
        }
        .feature-card {
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 15px;
            width: 45%;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }
        blockquote {
            border-left: 4px solid #ccc;
            padding-left: 10px;
            margin: 10px 0;
            color: #555;
        }
    </style>
</head>
<body>

<h1>🔐 Secure Auth System with PyQt5</h1>

<h2>✨ Key Features</h2>
<div class="features-grid">
    <div class="feature-card">
        <h3>🕒 Real-Time Clock</h3>
        <p>Homepage displays current time with automatic updates.</p>
    </div>
    <div class="feature-card">
        <h3>📧 Domain Validation</h3>
        <p>Restricts email registration to whitelisted domains.</p>
    </div>
    <div class="feature-card">
        <h3>🔐 Secure Storage</h3>
        <p>Encrypted credential storage in JSON format.</p>
    </div>
    <div class="feature-card">
        <h3>⚠️ Attempt Limiting</h3>
        <p>3 failed login attempts trigger account lockout.</p>
    </div>
</div>

<h2>🖥️ UI Components</h2>
<table>
    <tr>
        <th>Component</th>
        <th>Description</th>
    </tr>
    <tr>
        <td><strong>Login Window</strong></td>
        <td>Clean authentication interface with error handling.</td>
    </tr>
    <tr>
        <td><strong>Signup Form</strong></td>
        <td>Validation for email, password strength, and matching fields.</td>
    </tr>
    <tr>
        <td><strong>Home Screen</strong></td>
        <td>Welcome message with persistent navigation.</td>
    </tr>
</table>

<h2>🚀 Getting Started</h2>
<ol>
    <li><strong>Prerequisites</strong>
        <ul>
            <li>Python 3.8+</li>
            <li>PyQt5 (<code>pip install PyQt5</code>)</li>
        </ul>
    </li>
    <li><strong>Configuration</strong>
        <pre>
# Clone repository
git clone https://github.com/Rokerpro/login-signup_window.git

# Run application
python main.py
        </pre>
    </li>
</ol>

<h2>Customization</h2>
<ul>
    <li>Edit <code>VALID_DOMAINS</code> in <code>config.json</code>.</li>
    <li>Modify UI styles in <code>styles.qss</code>.</li>
    <li>Adjust attempt limit in <code>auth_settings.json</code>.</li>
</ul>

<h2>📝 Notes</h2>
<blockquote>
    <p>ℹ️ For production use, always implement proper password hashing (bcrypt, Argon2) before storing credentials.</p>
</blockquote>

<h2>💖 Contributing</h2>
<p>Pull requests welcome! Please follow PEP 8 guidelines and include tests for new features.</p>

<h2>📄 License</h2>
<p>MIT</p>

</body>
</html>
