<template>
  <div class="attribute-inner-container">
     <h1 class="text">{{ name }}</h1>
     <div class="value">{{ value }}</div>
     <img class="down_arrow" src="../assets/down_arrow.svg" alt="down_arrow" @click="decrease" />
     <img class="up_arrow" src="../assets/up_arrow.svg" alt="up_arrow" @click="increase" />
 </div>
</template>

<script>
   export default {
       name: "AttributeComponent",
       props: ['name', 'value'],  // Add 'value' to props
       methods: {
         increase() {
           this.$emit('increase', this.name);
         },
         decrease() {
           this.$emit('decrease', this.name);
         },
       },
   };
</script>
<style scoped>

.attribute-inner-container {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
  border-bottom: 1px solid #000000;
  border-top: 1px solid #000000;

}
 .text {
  font-size: 30px;
  line-height: 70px; /* Add this */
  width: 300px;
  height: 40px;
  text-align: left;
 }

 .value {
   font-size: 30px;
   margin-right: 60px;
   line-height: 40px;
   width: 20px;
 }

 .down_arrow {
   height: 40px;
 }

 .up_arrow {
   height: 40px;
   margin-left: 5px;
 }

</style>
