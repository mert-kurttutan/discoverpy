<script lang="ts" setup>
import { ref } from 'vue'

const PythonIndex = [
    "PyPI",
    "Anaconda",
]

const currentSource = ref(PythonIndex[0])
</script>

<template>
    <div class="index-source">
        <h2>Index Source</h2>
        <select v-model="currentSource">
            <option v-for="source in PythonIndex" :key="source">{{ source }}</option>
        </select>
    </div>
</template>

<style scoped>
/* // IndexSouce should be on the relative right side of the screen */

.index-source {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-right: 0;
    margin-left: auto;
}
</style>