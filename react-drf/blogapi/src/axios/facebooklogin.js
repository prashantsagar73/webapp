
import axios from 'axios';
import { useHistory } from 'react-router-dom';

const facebookLogin = (accesstoken) => {
	console.log(accesstoken);
	axios
		.post('http://127.0.0.1:8000/auth/convert-token', {
			token: accesstoken,
			backend: 'facebook',
			grant_type: 'convert_token',
			client_id: 't36PcCYVD85vDhKFIgAuCuk9wCjSjt2RBYL5ONmT',
			client_secret:
				'Nz9Jw4gEsyYdfl64W7ghN9HRDEzZtliNfLP25cKPI0DFPETRTLslYRKFlzQMvuUpNE1Nu8OaUGjnIHB8JEZWdo3zsKQT34j49zgNB63HSCquDBmCqyWboDVFuSiwdRao',
		})
		.then((res) => {
			localStorage.setItem('access_token', res.data.access_token);
			localStorage.setItem('refresh_token', res.data.refresh_token);
		});
};

export default facebookLogin;