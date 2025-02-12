<script lang="ts" setup>

// search bar component
import { ref, watchEffect } from 'vue'

import { routerPush, routerPushQuery } from '../router';

const search = ref('')

// watch for changes in the search bar

</script>

<template>
  <div class="search-bar">
    <!-- <input
      type="text"
      v-model="search"
      placeholder="Search for a python package..."
    />  add search button-->
    <input
      type="text"
      v-model="search"
      placeholder="Search for a python package..."
      @keyup.enter="routerPushQuery('search', {q: search})"
    />
    <button @click="routerPushQuery('search', {q: search})">Search</button>
    </div>
</template>


<style scoped>

.search-bar {
display: flex;
  justify-content: center;
  margin-top: 20px;
  margin-left: 0px;
    margin-right: 0px;
    padding-left: 0px;
    border-radius: 40px;

}

.search-bar input {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  border-radius: 150px;

}

.search-bar input:focus {
  outline: none;
}

</style>