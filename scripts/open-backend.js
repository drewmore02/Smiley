import 'dotenv/config';
import axios from 'axios';
import clipboardy from 'clipboardy';
import open from 'open';

async function openBackend() {
  const username = process.env.DJANGO_USERNAME;
  const password = process.env.DJANGO_PASSWORD;
  const apiUrl = process.env.DJANGO_LOGIN_API_URL;
  const swaggerUrl = process.env.SWAGGER_URL;

  if (!username || !password || !apiUrl || !swaggerUrl) {
    console.error('Missing environment variables. Check your .env file.');
    return;
  }

  try {
    const response = await axios.post(apiUrl, {
      username: username,
      password: password,
    });

    const accessToken = response.data.access;

    clipboardy.writeSync(`Bearer ${accessToken}`);
    console.log('Access token copied to clipboard!');

    await open(swaggerUrl);
    console.log('Swagger UI opened in browser.');

  } catch (error) {
    if (error.response) {
      console.error('Login failed:', error.response.data);
    } else {
      console.error('An error occurred:', error.message);
    }
  }
}

openBackend();