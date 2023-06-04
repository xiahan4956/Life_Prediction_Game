<template>
    <button class="player_feature" :class="{selected: isSelected}" @click="toggleSelection">{{feature}}</button>      
</template>

  

<script>
     export default {
         name: "FeatureComponent",
         props: ['feature'],
         data() {
             return {
                 isSelected: false,
             }
         },
         methods: {
             toggleSelection() {
                 this.isSelected = !this.isSelected;
                 if (this.isSelected) {
                     this.$emit('selected', this.feature);
                 } else {
                     this.$emit('deselected', this.feature);
                 }
             }
         }
     };
</script>
  

<style scoped>
    button{
        background-color: #ffffff;
    }

    .player_feature{
        width: 1000px;
        height: 50px;
        font-weight:normal;
        font-size: 19px;
        border: 1px solid #000000;
        border-radius: 10px;
        margin-top: 15px;
        display: flex;
        justify-content: center;
        align-items: center;
    }


    .selected{
        background-color: #CCCCCC;
    }
</style>
