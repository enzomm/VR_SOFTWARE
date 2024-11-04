import type { NavItem } from "@/types/Sidebar"
import { h } from "vue"
import { reactive } from "vue"
import { NotepadText } from "lucide-vue-next"

const navItems = reactive<NavItem[]>([
  { title: "Products", icon: h(NotepadText), link: "/" },  
]);

export default navItems;
