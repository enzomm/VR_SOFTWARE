<script setup lang="ts">
import { RouterView } from 'vue-router';
import Sidebar from '@/components/Sidebar.vue';
import Header from '@/components/Header.vue';
import { ref } from "vue";

const isOpen = ref<boolean>(true);    
</script>

<template>
    <div class="flex h-svh max-h-svh">
        <Sidebar v-model:toggleMenu="isOpen"/>
        <main class="bg-neutral-50 dark:bg-neutral-950 flex flex-col flex-1">
            <Header v-model:toggleMenu="isOpen"/>
            <section class="flex flex-col p-4 overflow-y-auto">
                <RouterView />
            </section>
        </main>
    </div>
</template>

<style scoped>
</style>
