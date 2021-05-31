import React, { useEffect, useState } from 'react';
import './App.css';
import Posts from './components/Posts';
import PostLoadingComponent from './components/PostLoading';

// to collect the data from django app through api 
function App() {
	const PostLoading = PostLoadingComponent(Posts);
	const [appState, setAppState] = useState({
		loading: false,
		posts: null,
	});
	// set connection through api 
	useEffect(() => {
		setAppState({ loading: true });
		// url of django app  make sure take care of http or https
		const apiUrl = `http://127.0.0.1:8000/api/`;
		fetch(apiUrl)
		// it Reflect the  data in json format 
			.then((data) => data.json())
			.then((posts) => {
				setAppState({ loading: false, posts: posts });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<h1>Latest Posts</h1>
			<PostLoading isLoading={appState.loading} posts={appState.posts} />
		</div>
	);
}
export default App;