import {
    Apple,   
    Beef
  } from 'lucide-vue-next'
import { h } from 'vue'

export const types = [
  {
    value: 'fruit',
    label: 'Fruit',
    icon: h(Apple),
  },
  {
    value: 'meat',
    label: 'Meat',
    icon: h(Beef),
  },  
]
