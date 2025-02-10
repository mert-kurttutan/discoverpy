<script lang="ts" setup>
import { ref } from 'vue';
import SearchBar from './SearchBar.vue';
import CategorySummary from './CategorySummary.vue';
import IndexSource from './IndexSource.vue';
import CombineLeftRight from './CombineLeftRight.vue';
import PagesTab from './PagesTab.vue';
import Stats from './Stats.vue';

// get the current page from PagesTab
const currentPage = ref('Categories');
</script>

<template>
  <CombineLeftRight>
    <template #left>
      <PagesTab v-model="currentPage"/>
    </template>
    <template #right>
      <IndexSource />
    </template>
  </CombineLeftRight>
  <SearchBar />

  <!-- <CategorySummary /> -->
  <RouterView />
  <CategorySummary v-if="currentPage === 'Categories'"/>
  <Stats v-if="currentPage === 'Stats'"/>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

/* // IndexSouce should be on the right side of the screen */
.index-source1 {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  margin-right: 0;
  margin-left: auto;
}
</style>
