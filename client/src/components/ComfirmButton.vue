
<template>
    <div class="comfirm_button">
        <div class="text">{{ text }}</div>
    </div>
  </template>
  
  <script>
    export default {
      name: "ComfirmButton",
      props: ["text"],
    };
  </script>
  
  <style scoped>
    .comfirm_button{
      width: 300px;
      height: 40px;
      border: 2px solid #000000;
      border-radius: 30px;
      background-color: #FFFFFF;
      transition: background-color 0.1s; 
    }

    .comfirm_button:hover{
      background-color: #CCCCCC;
    }


    .text{
      font-weight: 400;
      font-size: 24px;
      line-height: 30px;
      color: #333333;
      text-align: center;
      margin-top: 5px
    }
  
  </style>