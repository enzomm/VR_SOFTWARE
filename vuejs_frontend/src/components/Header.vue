<script setup lang="ts">
import { Avatar } from '@/components/ui/avatar';
import {  
  Keyboard,
  LifeBuoy,  
  Settings,
  User,  
  Bell,
  PanelLeftOpen,
  PanelLeftClose,
  UserRound,
  Menu,
  SunMoon
} from 'lucide-vue-next'
import { Button } from '@/components/ui/button';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuGroup,
  DropdownMenuItem,
  DropdownMenuLabel,  
  DropdownMenuSeparator,
  DropdownMenuShortcut,  
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { Toggle } from '@/components/ui/toggle'
import {
  Sheet,
  SheetContent,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
  SheetClose
} from '@/components/ui/sheet'

import SidebarMobile from "@/components/SidebarMobile.vue";

const isOpen = defineModel("toggleMenu", {required:true});

function handleToggleMenu() {
  return isOpen.value = !isOpen.value;
}

function handleToggleTheme() {
  document.documentElement.classList.toggle('dark')
}
</script>

<template>
  <header class="flex h-12 flex-row justify-between items-center gap-2 bg-neutral-200 dark:bg-neutral-900 border-b-2 border-neutral-300 dark:border-neutral-800 transition-all">      
    <div>
      <Button @click="handleToggleMenu()" variant="outline" class="hidden xl:inline-block p-2 ml-1 bg-neutral-200 dark:bg-neutral-900 dark:text-zinc-300 text-zinc-900 dark:hover:text-sky-500 hover:text-sky-500 dark:hover:bg-neutral-800 hover:bg-neutral-100 shadow-none">
        <PanelLeftClose v-if="isOpen" :size=20 :stroke-width=2 />
        <PanelLeftOpen v-else :size=20 :stroke-width=2 />
      </Button>
      <Sheet>
        <SheetTrigger class="md:hidden">
          <Button variant="outline" class="p-2 ml-1 bg-neutral-200 dark:bg-neutral-900 dark:text-zinc-300 text-zinc-900 dark:hover:text-sky-500 hover:text-sky-500 dark:hover:bg-neutral-800 hover:bg-neutral-100 shadow-none">
            <Menu :size=20 :stroke-width=2 />
          </Button>
        </SheetTrigger>
        <SheetContent class="dark:bg-slate-950 bg-slate-100" side="left">
          <SheetHeader>
            <SheetTitle>Menu</SheetTitle>
          </SheetHeader>
          <SheetClose as-child>
            <SidebarMobile />
          </SheetClose>
        </SheetContent>
      </Sheet>
    </div>

    <div class="inline-flex justify-center items-center gap-4 p-2">
      <Toggle @click="handleToggleTheme" class="dark:bg-neutral-900 bg-neutral-200 dark:text-zinc-300 text-zinc-800 dark:hover:text-sky-500 hover:text-sky-500 dark:hover:bg-neutral-800 hover:bg-neutral-100 shadow-none" >
        <SunMoon :size=22 :stroke-width=2 />
      </Toggle>

      <DropdownMenu>
        <DropdownMenuTrigger>
          <Button variant="outline" class="dark:bg-neutral-900 bg-neutral-200 dark:text-zinc-300 text-zinc-800 dark:hover:text-sky-500 hover:text-sky-500 dark:hover:bg-neutral-800 hover:bg-neutral-100 shadow-none" size="icon">
            <Bell class="" :size=20 :stroke-width=2 />
          </Button>
        </DropdownMenuTrigger>
        <DropdownMenuContent>
          <DropdownMenuLabel>Notifications</DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuItem>Message 1</DropdownMenuItem>
          <DropdownMenuItem>Message 2</DropdownMenuItem>
          <DropdownMenuItem>Message 3</DropdownMenuItem>          
        </DropdownMenuContent>
      </DropdownMenu>

      <DropdownMenu>
        <DropdownMenuTrigger>
            <Avatar size="sm">
                <UserRound :size=22 :stroke-width=2 />
            </Avatar>
        </DropdownMenuTrigger>
        <DropdownMenuContent class="w-56">
          <DropdownMenuLabel>My Account</DropdownMenuLabel>
          <DropdownMenuSeparator />
          <DropdownMenuGroup>
            <DropdownMenuItem>
              <User class="mr-2 h-4 w-4" />
              <span>Profile</span>
              <DropdownMenuShortcut>⇧⌘P</DropdownMenuShortcut>
            </DropdownMenuItem>            
            <DropdownMenuItem>
              <Settings class="mr-2 h-4 w-4" />
              <span>Settings</span>
              <DropdownMenuShortcut>⌘S</DropdownMenuShortcut>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <Keyboard class="mr-2 h-4 w-4" />
              <span>Keyboard shortcuts</span>
              <DropdownMenuShortcut>⌘K</DropdownMenuShortcut>
            </DropdownMenuItem>
          </DropdownMenuGroup>
          <DropdownMenuSeparator />
          <DropdownMenuItem>
            <LifeBuoy class="mr-2 h-4 w-4" />
            <span>Support</span>
          </DropdownMenuItem>
        </DropdownMenuContent>
      </DropdownMenu>
    </div>
  </header>
</template>

<style scoped>
</style>
