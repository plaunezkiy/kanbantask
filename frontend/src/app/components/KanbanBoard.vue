<template>
	<div class="kanban-board">
		<div class="row">
			<h3 class="header orange">On Hold ({{items[0].length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload0" @drop="onDrop(0, $event)">
				<Draggable v-for="item in items[0]" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem(0, item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.header}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title0" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[0]"></textarea>
			<button class="add-a-card" @click="addItem(0)" v-bind:style="addACardStyle[0]">Добавить карточку1</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[0]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(0)" v-bind:style="addAnotherCardStyle[0]">Добавить карточку</button>
		</div>
		<div class="row">
			<h3 class="header blue">In Progress ({{items[1].length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload1" @drop="onDrop(1, $event)">
				<Draggable v-for="item in items[1]" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem(1, item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.header}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title1" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[1]"></textarea>
			<button class="add-a-card" @click="addItem(1)" v-bind:style="addACardStyle[1]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[1]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(1)" v-bind:style="addAnotherCardStyle[1]">Добавить карточку</button>
		</div>
		<div class="row">
			<h3 class="header yellow">Needs Review ({{items[2].length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload2" @drop="onDrop(2, $event)"> 
				<Draggable v-for="item in items[2]" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem(2, item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.header}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title2" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[2]"></textarea>
			<button class="add-a-card" @click="addItem(2)" v-bind:style="addACardStyle[2]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[2]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(2)" v-bind:style="addAnotherCardStyle[2]">Добавить карточку</button>
		</div>
		<div class="row">
			<h3 class="header green">Approved ({{items[3].length}})</h3>
			<Container :group-name="'1'" :get-child-payload="getChildPayload3" @drop="onDrop(3, $event)">
				<Draggable v-for="item in items[3]" :key="item.id">
					<div class="draggable-item">
						<div class="delete" @click="deleteItem(3, item)"></div>
						<p><b class="id">id: </b>{{item.id}}</p>
						<p>{{item.header}}</p>
					</div>
				</Draggable>
			</Container>
			<textarea id="title3" class="card-title-textarea" rows="5" placeholder="Ввести заголовок для этой карточки" v-model="newCardHeader" v-bind:style="addACardStyle[3]"></textarea>
			<button class="add-a-card" @click="addItem(3)" v-bind:style="addACardStyle[3]">Добавить карточку</button>
			<button class="cancel" @click="hideAddACardTextarea()" v-bind:style="addACardStyle[3]"></button>
			<button class="add-another-card" @click="showAddACardTextarea(3)" v-bind:style="addAnotherCardStyle[3]">Добавить карточку</button>
		</div>
	</div>
</template>

<script>
import axios from 'axios'
import { Container, Draggable } from "vue-smooth-dnd";
import { applyDrag } from "./utils";
export default {
	name: "KanbanBoard",
	components: { Container, Draggable },
	props: {
		items: Array,
	},
	data: function() {
		return {
			newCardHeader: '',
			addACardStyle: [ 
					{ display: 'none'},
					{ display: 'none'},
					{ display: 'none'},
					{ display: 'none'}
				],
			addAnotherCardStyle: [ 
					{ display: 'block'},
					{ display: 'block'},
					{ display: 'block'},
					{ display: 'block'}
				],
		};
	},
	methods: {
		onDrop: function(collection, dropResult) {
			this.hideAddACardTextarea();
			this.items.splice(collection, 1, applyDrag(this.$parent.items[collection], dropResult));
			if (collection === 3) {
				this.resortItems();
			}
		},
		getChildPayload0(index) {
   			return this.items[0][index];
  		},
		getChildPayload1(index) {
   			return this.items[1][index];
  		},
		getChildPayload2(index) {
   			return this.items[2][index];
  		},
		getChildPayload3(index) {
   			return this.items[3][index];
  		},
		addItem: function(collection) {
			if (this.$parent.user) {
				if (this.newCardHeader) {
					axios({
						method: 'post',
						url: 'http://localhost:8000/v1/cards/',
						headers: {'Authorization': 'JWT ' + localStorage.token},
						data: {'header': this.newCardHeader, 'status': collection+1},
					})
					.then(resp => {
						this.items[collection].push(resp.data);
					})
					this.hideAddACardTextarea();
				}
			}
		},
		deleteItem: function(collection, item) {
			let index = this.items[collection].map(x => {
				return x.id;
			}).indexOf(item.id);
			if (this.$parent.user) {
				axios.delete(
					'http://localhost:8000/v1/cards/'+item.id, 
					{'headers': {'Authorization': 'JWT ' + localStorage.token}}
				)
				.then(resp => {this.items[collection].splice(index, 1)})
			}
		},
		resortItems: function() {
			axios({
				method: 'post',
				url: 'http://localhost:8000/v1/resort/',
				headers: {'Authorization': 'JWT ' + localStorage.token},
				data: this.items.map((column) => {
					return column.map(x => {
						return x.id;
					})
				}),
			})
		},
		hideAddACardTextarea: function() {
			this.newCardHeader = '';
			for(let i = 0; i < this.addACardStyle.length; i++) {
				this.addACardStyle[i].display = 'none';
			}
			for(let i = 0; i < this.addAnotherCardStyle.length; i++) {
				this.addAnotherCardStyle[i].display = 'block';
			}
		},
		showAddACardTextarea: function(col) {
			this.hideAddACardTextarea();
			this.addAnotherCardStyle[col].display = 'none';
			this.addACardStyle[col].display = 'block';
			let textareaID = 'title' + col.toString();

			setTimeout(function() {
				document.getElementById(textareaID).focus();
			}, 0);
		}
	}
};
</script>