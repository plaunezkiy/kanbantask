<template>
<div :class="'app'">
	<nav class="navbar navbar-dark bg-dark px-2">
		<a class="navbar-brand" href="/">Kanban</a>
		<g-signin-button
            v-if="isEmpty(user)"
            :params="googleSignInParams"
            @success="onGoogleSignInSuccess"
            @error="onGoogleSignInError"
          >
            <button class="btn btn-block btn-success">
              Google Signin
            </button>
          </g-signin-button>
          <user-panel v-else :user="user"></user-panel>
    </nav>
	<div class="container">
      <div class="columns" style="margin-top: 100px;">
        <div class="column col-2 centered">
        </div>
      </div>
	  <KanbanBoard 
	  	:items="items">
	  </KanbanBoard>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import UserPanel from './components/UserPanel'
import { KanbanBoard } from './components';
import { loadItems } from "./components/utils";
export default {
	name: "App",
	components: {
		UserPanel,
		KanbanBoard,
	},
	data () {
		return {
			user: {},
			items: [[], [], [], []],
			googleSignInParams: {
				client_id: '948567136290-h1eshhdpmmjs4n0ke94q3tbld6b91v7t.apps.googleusercontent.com'
			}
		}
	},
	beforeMount() {
		if (localStorage.user) {
			this.user = JSON.parse(localStorage.user);
			this.items = loadItems();
		}
	},
	methods: {
		onGoogleSignInSuccess (resp) {
			const token = resp.tc.access_token
			axios.post('http://localhost:8000/auth/google/', {
				access_token: token
			})
			.then(resp => {
				localStorage.token = resp.data.token
				localStorage.user = JSON.stringify(resp.data.user)
				this.user = resp.data.user
				this.items = loadItems();
			})
			.catch(err => {
				console.log(err.response)
			})
		},
		onGoogleSignInError (error) {
			console.log(error)
		},
		isEmpty (obj) {
			return Object.keys(obj).length === 0
		},
	}

};
</script>

<style src="../style.css"/>

