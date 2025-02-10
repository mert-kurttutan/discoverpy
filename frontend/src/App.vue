<script lang="ts" setup>
import HelloWorld from './components/HelloWorld.vue'
import { ref } from 'vue';
import SearchBar from './components/SearchBar.vue';
import CategorySummary from './components/CategorySummary.vue';
import IndexSource from './components/IndexSource.vue';
import CombineLeftRight from './components/CombineLeftRight.vue';
import PagesTab from './components/PagesTab.vue';
import Stats from './components/Stats.vue';

// get the current page from PagesTab
const currentPage = ref('Categories');
</script>

<template>
  # divide index-source1 into two parts horizontally
  <CombineLeftRight>
    <template #left>
      <SearchBar />
    </template>
    <template #right>
      <IndexSource />
    </template>
  </CombineLeftRight>
  <PagesTab v-model="currentPage"/>
  <!-- <CategorySummary /> -->
   # activate CategorySummary component if the current page is 'Categories'
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
