<template>
    <div class="dropdown">
      <a class="dropdown-toggle btn btn-outline-success" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
        {{ user.username }}
      </a>
      <ul class="dropdown-menu dropdown-menu-right" style="right:0; left:auto;">
        <li>
          <button class="dropdown-item">
            {{ user.first_name }} {{ user.last_name }}
            <br>
            {{ user.email }}
          </button>
        </li>
        <hr class="dropdown-divider">
        <li><button class="dropdown-item" @click="logout">Logout</button></li>
      </ul>
    </div>
</template>
<script>
export default {
  name: 'UserPanel',
  props: ['user',],
  methods: {
    logout () {
      this.$parent.user = {};
      this.$parent.items = [[], [], [], []];
			localStorage.removeItem('token');
			localStorage.removeItem('user');
		},
  },
}
</script>