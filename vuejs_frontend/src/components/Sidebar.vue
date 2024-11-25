<script setup lang="ts">
import { RouterLink } from 'vue-router';
import { LifeBuoy } from 'lucide-vue-next';
import navItems from '@/data/navItems';

const isOpen = defineModel("toggleMenu", {required:true});
</script>

<template>
    <aside class="hidden md:flex md:flex-col md:w-16 dark:bg-slate-950 bg-slate-100 transition-all" :class="[isOpen ? 'xl:w-56' : 'xl:w-16']">
        <header class="flex h-12 justify-center items-center bg-red-600 shadow-md">
            <a href="#" class="hidden text-2xl text-zinc-300 font-bold" :class="[isOpen ? 'xl:flex' : 'xl:hidden']">
                <img class="h-10" src="@/assets/logo.png" alt="Logo"/>
            </a>
            <a href="#" class="text-2xl text-zinc-300 font-bold" :class="[isOpen ? 'xl:hidden' : 'xl:flex']">
                <img class="h-10" src="@/assets/icon_logo.png" alt="Icone Logo"/>
            </a>
        </header>

        <nav class="flex flex-1 flex-col justify-between shadow-2xl border-r-2 dark:border-slate-900 border-slate-300">
            <ul class="flex flex-col gap-2 px-2 mt-4">
                <li v-for="ni in navItems" class="flex justify-start">
                    <RouterLink class="flex w-full items-center gap-3 px-3 py-2 rounded-lg dark:text-zinc-600 text-zinc-700 dark:hover:text-zinc-300 hover:text-zinc-900 dark:hover:bg-slate-900 hover:bg-slate-200 transition" :to="ni.link">
                        <component :is="ni.icon" class="icon" size=22 stroke-width=2 />
                        <span v-if="isOpen" class="hidden text-sm xl:inline-block">{{ ni.title }}</span>
                    </RouterLink>
                </li>
            </ul>

            <ul class="flex flex-col gap-2 px-2 mt-4 mb-2">
                <!-- Nav Item -->
                <li class="flex items-center justify-start xl:w-full">
                    <RouterLink class="flex w-full items-center gap-3 px-3 py-2 rounded-lg dark:text-zinc-600 text-zinc-700 dark:hover:text-zinc-300 hover:text-zinc-900 dark:hover:bg-slate-900 hover:bg-slate-200 transition" to="/">
                        <LifeBuoy :size=22 :stroke-width=2 class="icon" />
                        <span v-if="isOpen" class="hidden text-sm xl:inline-block">Support</span>
                    </RouterLink>
                </li>
                <!-- Separador -->   
                <hr class="h-px mt-0 bg-transparent bg-gradient-to-r from-transparent via-black/40 to-transparent"/>
                <!-- Info -->
                <div class="w-full flex flex-col items-center">
                    <p class="text-sm font-normal text-opacity-50 uppercase">
                        Loopia
                    </p>
                    <p class="mb-0 text-xs font-light text-opacity-50">
                        Version 1.0.0
                    </p>                          
                </div>
            </ul>
        </nav>
    </aside>
</template>

<style scoped>
</style>
