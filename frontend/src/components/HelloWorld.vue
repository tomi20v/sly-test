<script setup lang="ts">
  import { ref } from 'vue'
  
  defineProps<{ msg: string }>()
  
  const count = ref(0)
  </script>
  
  <template>
  <v-container>
    <v-row class="text-center">
      <v-col class="mb-4">
        <h1 class="display-2 font-weight-bold mb-3">
          Welcome to Vuetify {{ msg }}
        </h1>

        <p class="subheading font-weight-regular">
          For help and collaboration with other Vuetify developers,
          <br>please join our online
          <a
            href="https://community.vuetifyjs.com"
            target="_blank"
          >Discord Community</a>
        </p>
        <v-btn
          class="text-none mb-4"
          color="indigo-darken-3"
          size="x-large"
          variant="flat"
          block
          prepend-icon="mdi-truck"
          @click="count++"
        >click me {{ count }}</v-btn>
        <v-alert text="lorem ipsum dolor sit amet" title="alert title" type="success"></v-alert>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup lang="ts">
</script>
