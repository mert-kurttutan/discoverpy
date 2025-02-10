<script lang="ts" setup>
const Pages = [
    "Search",
    "Categories",
    "Stats",
    "About",
]

// const currentPage = ref(Pages[0])
const currentPage = defineModel<string>()

</script>

// horizontal tab bar, with active tab highlighted

<template>
    <div class="pages-tab">
        <ul>
            <li v-for="page in Pages" :key="page" :class="{ active: page === currentPage }" @click="currentPage = page">{{ page }}</li>
        </ul>
    </div>
</template>

<style scoped>

.pages-tab {
    display: flex;
    justify-content: center;
    margin-top: 20px;
    /* background-color:forestgreen; */
    border-width: 40px;
    border-color: white;
}

.pages-tab ul {
    display: flex;
    list-style-type: none;
    padding: 0;
}

.pages-tab li {
    margin: 0 10px;
    cursor: pointer;
}

.pages-tab li.active {
    /* color: blue; */
    font-weight: bold;
    text-decoration: underline;
}
</style>