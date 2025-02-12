<script lang="ts" setup>
import { Bar, Scatter } from 'vue-chartjs'
import { Chart as ChartJS,   LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend } from 'chart.js'
  import * as chartConfig from '../store/scatterDataset'

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend)
const chartOptions = {
  responsive: true,
//   maintainAspectRatio: false
}

</script>

<template>
  <div>
    <p>Package to Anaylze: {{ $route.query.q }}</p>
  </div>

  <Scatter
    id="my-chart-id"
    :options="chartConfig.options"
    :data="chartConfig.data"
  />
</template>