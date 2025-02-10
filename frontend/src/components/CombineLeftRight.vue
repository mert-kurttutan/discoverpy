<script lang="ts" setup>
</script>

<template>
    <div class="container">
      <div class="left">
        <slot name="left"></slot> <!-- Slot for Left Component Content -->
      </div>
      <div class="right">
        <slot name="right"></slot> <!-- Slot for Right Component Content -->
      </div>
    </div>
  </template>
  
  <style scoped>
  .container {
    display: flex;
    /* width: 100vw; */
    /* height: 100vh; */
    align-items: center; /* Centers the left box vertically */
  }
  .left {
    width: 90%;
    /* background-color: lightblue; */
    /* display: flex; */
    flex:2;
    justify-content: center;
    align-items: center;
    height: 100px;
    margin-left: 0px;
    margin-right: 0px;
    padding-left: 0px;
  }
  .right {
    width: 10%;
    /* display: flex; */
    flex:1;
    flex-direction: column;
    /* background-color: lightcoral; */
    justify-content: center;
    align-items: center;
    height: 100px;
  }
  </style>
  