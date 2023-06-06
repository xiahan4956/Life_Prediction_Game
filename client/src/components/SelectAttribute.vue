<template>
  <div class="page_container"> 
      <h1 class="title">Distribute your innate  atrributes(2/3)</h1>

      <div class="attribute-main-container">
          <div class="intro"> Points Available to Distribute: {{ points }} </div>
          <attribute-component 
            v-for="attribute in attributes" 
            :key="attribute" 
            :name="attribute"
            :value="attributeValues[attribute]" 
            @increase="increaseAttribute"
            @decrease="decreaseAttribute"
          ></attribute-component>
      </div>

      <comfirm-button class="main_button" text="Next"  @click = "next_page" />
  </div>
</template>
<script>
  import ComfirmButton from './ComfirmButton.vue';
  import AttributeComponent from './AttributeComponent.vue';

  export default {
      name: "SelectAttribute",
      components: {
          ComfirmButton,
          AttributeComponent,
      },
      data() {
        return {
          points: 20,
          attributes: ['beauty', 'family', 'health', 'intelligence'],
          attributeValues: {
            beauty: 0,
            family: 0,
            health: 0,
            intelligence: 0,
          },
          hasSetFeatures: false, // Add this flag
        };
      },
      methods: {
          increaseAttribute(attribute) {
              if (this.points > 0 && this.attributeValues[attribute] < 10) {
                this.attributeValues[attribute]++;
                this.points--;
              }
              },
            decreaseAttribute(attribute) {
            if (this.attributeValues[attribute] > 0) {
              this.attributeValues[attribute]--;
              this.points++;
            }
            },
          async next_page() {
              if (!this.hasSetFeatures) { // Check the flag here
                  alert('Please wait a moment to load features...');
                  return;
              }
              if (this.points == 0) {
                  try {
                      const response = await this.$http.post('http://qq4956.pythonanywhere.com/api/distributed_attribute', {
                          health: this.attributeValues.health,
                          family: this.attributeValues.family,
                          intelligence: this.attributeValues.intelligence,
                          beauty: this.attributeValues.beauty
                      });

                      if (response.data.dead_age) {
                          const  dead_age = response.data.dead_age;

                          // 保存属性到localStorage
                          localStorage.setItem('attributes', JSON.stringify(this.attributeValues));
                          localStorage.setItem('dead_age', dead_age)

                          this.$router.push({name: 'SelectFeatures'});
                      } else {
                          // handle error response
                          console.error('Error in response:', response); 
                      }
                  } catch (error) {
                      console.error(error);
                  }
              } else {
                  alert("Please distribute all points");
              }
            }
          },
         
      async mounted() {
          const selectedStyle = this.$route.params.feature;
          try {
              const response = await this.$http.post('http://qq4956.pythonanywhere.com/api/selected_game_style', {selected_game_style: selectedStyle});

              const potential_features = response.data.potential_features;

              localStorage.setItem('game_style', selectedStyle);
              localStorage.setItem('potentialFeatures', JSON.stringify(potential_features));
              this.hasSetFeatures = true; // Set the flag here
          } catch (error) {
              console.error(error);
          }
      },
  };  
</script>


<style scoped>
.page_container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height:  70vh;
}



.title {
  font-weight: 400;
  font-size: 60px;
  line-height: 24px;
  color: #333333;
}

.intro{
  font-weight: 400;
  font-size: 20px;
}

.attribute-main-container{
display: flex;
flex-direction: column;
}


.main_button {
    margin-top: 100px;
  }

</style>
