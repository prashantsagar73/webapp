import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';

const routing =(
    <Router>
		<React.StrictMode>
			<Header />
			<Switch>
				<Route exact path="/" component={App} />
			</Switch>
			<Footer />
		</React.StrictMode>
	</Router>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
ReactDOM.render(routing, document.getElementById('root'));
serviceWorker.unregister();