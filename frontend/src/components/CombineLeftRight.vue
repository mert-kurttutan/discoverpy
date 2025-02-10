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
  
  <script>
  export default {
    name: 'LayoutComponent'
  };
  </script>
  
  <style scoped>
  .container {
    display: flex;
    width: 100vw;
    /* height: 100vh; */
    align-items: center; /* Centers the left box vertically */
  }
  .left {
    width: 70%;
    /* background-color: lightblue; */
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100px;
  }
  .right {
    width: 30%;
    /* background-color: lightcoral; */
    height: 100px;
    margin-left: auto; /* Pushes right div to the far right */
  }
  </style>
  