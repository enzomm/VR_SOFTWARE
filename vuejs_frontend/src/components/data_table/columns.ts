import type { ColumnDef } from '@tanstack/vue-table'
import type { Product } from '@/data/schema'
import { Checkbox } from '@/components/ui/checkbox'
import { h } from 'vue'
import DataTableColumnHeader from './DataTableColumnHeader.vue'
import DataTableRowActions from './DataTableRowActions.vue'
import { DollarSign } from "lucide-vue-next"
import { types } from '@/data/data'

export const columns: ColumnDef<Product>[] = [
  {
    id: 'select',
    header: ({ table }) => h(Checkbox, {
      'checked': table.getIsAllPageRowsSelected() || (table.getIsSomePageRowsSelected() && 'indeterminate'),
      'onUpdate:checked': value => table.toggleAllPageRowsSelected(!!value),
      'ariaLabel': 'Select all',
      'class': 'translate-y-0.5',
    }),
    cell: ({ row }) => h(Checkbox, { 'checked': row.getIsSelected(), 'onUpdate:checked': value => row.toggleSelected(!!value), 'ariaLabel': 'Select row', 'class': 'translate-y-0.5' }),
    enableSorting: false,
    enableHiding: false,
  },
  {
    accessorKey: 'id',
    header: ({ column }) => h(DataTableColumnHeader, { column, title: 'Code' }),
    cell: ({ row }) => h('div', { class: 'w-20' }, row.getValue('id')),
    enableSorting: false,
    enableHiding: false,
  },  
  {
    accessorKey: 'image',
    header: ({ column }) => h(DataTableColumnHeader, { column, title: 'Image' }),

    cell: ({ row }) => {
      return h('div', { class: 'flex items-center' }, [        
        h('img', { class: 'size-8 rounded border shadow', src: row.getValue('image'), alt: 'Image' }),
      ])
    },    
  },
  {
    accessorKey: 'description',
    header: ({ column }) => h(DataTableColumnHeader, { column, title: 'Description' }),

    cell: ({ row }) => {
      return h('div', { class: 'flex space-x-2' }, [            
        h('span', { class: 'max-w-[500px] truncate font-medium' }, row.getValue('description')),
      ])
    },
  },
  {
    accessorKey: 'cost',
    header: ({ column }) => h(DataTableColumnHeader, { column, title: 'Cost' }),

    cell: ({ row }) => {
      return h('div', { class: 'flex w-[100px] items-center' }, [        
        h(DollarSign) && h(h(DollarSign), { class: 'mr-2 h-4 w-4 text-muted-foreground' }), 
        h('span', row.getValue('cost')),
      ])
    },    
  },  
  {
    accessorKey: 'type',
    header: ({ column }) => h(DataTableColumnHeader, { column, title: 'Type' }),

    cell: ({ row }) => {
      const type = types.find(
        type => type.value === row.getValue('type'),
      )

      if (!type)
        return null

      return h('div', { class: 'flex w-[100px] items-center' }, [
        type.icon && h(type.icon, { class: 'mr-2 h-4 w-4 text-muted-foreground' }),
        h('span', type.label),
      ])
    },
    filterFn: (row, id, value) => {
      return value.includes(row.getValue(id))
    },
  },
  {
    id: 'actions',
    cell: ({ row }) => h(DataTableRowActions, { row }),
  },
]
