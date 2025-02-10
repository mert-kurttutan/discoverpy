<script lang="ts" setup>


import { ref } from 'vue'

const Stats = [
    "Total",
    "Unique",
    "Popular",
    "New",
]

const currentStat = ref(Stats[0])

</script>

<template>
    <div class="stats">
        <h2>Stats</h2>
        <select v-model="currentStat">
            <option v-for="stat in Stats" :key="stat">{{ stat }}</option>
        </select>
    </div>
</template>