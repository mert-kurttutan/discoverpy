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
        <p>Index Source: </p>
        <select v-model="currentSource">
            <option v-for="source in PythonIndex" :key="source">{{ source }}</option>
        </select>
    </div>
</template>

<style scoped>
/* // IndexSouce should be on the relative right side of the screen */

.index-source {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-top: 20px;
    margin-left: 10px;

}

p {
    /* margin: 0 10px; */
    /* margin-top: 20px; */
    margin-right: 10px;
    padding: 0;
}
</style>