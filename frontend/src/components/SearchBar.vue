<script lang="ts" setup>

// search bar component
import { ref, watchEffect } from 'vue'

const search = ref('')

// watch for changes in the search bar
watchEffect(() => {
  console.log(search.value)
})

</script>

<template>
  <div class="search-bar">
    <input
      type="text"
      v-model="search"
      placeholder="Search for a movie..."
    />
    </div>
</template>
