<script lang="ts" setup>

import { computed, ref, watchEffect } from 'vue'

import { CategoryList } from '../store/CategoryStore'

// compute array width from screen size
// when full size, 4 columns
// when medium size, 3 columns
// when small size, 2 columns
// when extra small size, 1 column
const columns = ref(4)
const screenWidth = ref(window.innerWidth)

window.addEventListener('resize', () => {
    screenWidth.value = window.innerWidth
})

watchEffect(() => {
    // console.log("screen width: ", screenWidth.value);
    if (screenWidth.value >= 1200) {
        columns.value = 4
    } else if (screenWidth.value >= 750) {
        columns.value = 3
    } else if (screenWidth.value >= 500) {
        columns.value = 2
    } else {
        columns.value = 1
    }
})

// now compute the number of rows from the number of columns
const rows = computed(() => Math.ceil(24 / columns.value))

</script>

<template>
    <div class="category-list">
        <h2>Categories</h2>
        <div class="row" v-for="i in rows" :key="i">
            <div class="column" v-for="j in columns" :key="j">
                <div class="card">
                    <h3>{{ CategoryList[(i-1)*columns+j-1].name }}</h3>
                    <p>{{ CategoryList[(i-1)*columns+j-1].description }}</p>
                </div>
            </div>
        </div>
    </div>
</template>


<style scoped>

.category-list {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.row {
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.column {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

</style>