<script setup lang="ts">
import { RouterLink } from 'vue-router';
import navItems from '@/data/navItems';
import { LifeBuoy } from 'lucide-vue-next';
</script>

<template>
    <nav class="flex flex-1 flex-col justify-between w-full">
        <ul class="flex flex-col gap-2 px-2 mt-4">
            <li v-for="ni in navItems" class="flex justify-start">
                <RouterLink class="flex w-full items-center gap-3 px-3 py-2 rounded-lg dark:text-zinc-600 text-zinc-700 dark:hover:text-zinc-300 hover:text-zinc-900 dark:hover:bg-slate-900 hover:bg-slate-200 transition" :to="ni.link">
                    <component :is="ni.icon" class="icon" size=22 stroke-width=2 />
                    <span class="text-sm">{{ ni.title }}</span>
                </RouterLink>
            </li>
        </ul>

        <ul class="flex flex-col gap-2 px-2 mt-2 mb-2">
            <li class="flex items-center justify-start xl:w-full">
                <RouterLink class="flex w-full items-center gap-3 px-3 py-2 rounded-lg dark:text-zinc-600 text-zinc-700 dark:hover:text-zinc-300 hover:text-zinc-900 dark:hover:bg-slate-900 hover:bg-slate-200 transition" to="/">
                    <LifeBuoy :size=22 :stroke-width=2 class="icon" />
                    <span class="text-sm">Support</span>
                </RouterLink>
            </li>
        </ul>
    </nav>
</template>

<style scoped>
</style>
