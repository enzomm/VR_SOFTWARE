<script setup lang="ts">
import { Button } from '@/components/ui/button'
import {  
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form'
import { vAutoAnimate } from '@formkit/auto-animate'
import { toTypedSchema } from '@vee-validate/zod'
import { useForm } from 'vee-validate'
import * as z from 'zod'
import FileInput from '@/components/FileInput.vue'
import { Textarea } from '@/components/ui/textarea'
import {
  NumberField,
  NumberFieldContent,
  NumberFieldDecrement,
  NumberFieldIncrement,
  NumberFieldInput,
} from '@/components/ui/number-field'
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
  CommandList,
} from '@/components/ui/command'
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import { cn } from '@/lib/utils'
import { CaretSortIcon, CheckIcon } from '@radix-icons/vue'
import { defineProps, watch, ref } from 'vue'

const types = [
  { label: 'Meat', value: 'meat' },
  { label: 'Fruit', value: 'fruit' }, 
] as const

const formSchema = toTypedSchema(z.object({
  image: z.any().refine(val => val instanceof File || (val instanceof FileList && val.length > 0), {
    message: 'Required.'
  }),
  description: z
    .string()
    .min(10, {
      message: 'Must be at least 10 characters.',
    })
    .max(255, {
      message: 'Must not be longer than 255 characters.',
    }),
  cost: z.number().min(1, 'Min 1 real.').max(1000, 'Max 1000 reais.'),
  type: z.string({
    required_error: 'Please select a type.',
  }),
}))

const props = defineProps<{ 
  onSubmit: (values: any) => void,
  initialValues?: Partial<{ image: any, description: string, cost: number, type: string }>
}>()

const { isFieldDirty, handleSubmit, setFieldValue, values, setValues } = useForm({
  validationSchema: formSchema,
  initialValues: props.initialValues || {
    image: null,
    description: '',
    cost: 10,
    type: '',
  },
})

watch(() => props.initialValues, (newVal) => {
  if (newVal) {
    setValues(newVal)    
  }
})

const hS = handleSubmit(props.onSubmit)
</script>

<template>
    <form id="product-form" class="grid items-start gap-4 px-4" @submit="hS">      
      <FormField v-slot="{ componentField }" name="image" :validate-on-blur="!isFieldDirty" class="grid gap-2">
        <FormItem v-auto-animate>
          <FormLabel>Image</FormLabel>
          <FormControl>
            <FileInput v-bind="componentField" accept="image/png, image/jpeg" />
          </FormControl>
          <FormDescription>
            What is the product image?
          </FormDescription>
          <FormMessage />
        </FormItem>
      </FormField>
      <FormField v-slot="{ componentField }" name="description" :validate-on-blur="!isFieldDirty" class="grid gap-2">
        <FormItem v-auto-animate>
          <FormLabel>Description</FormLabel>
          <FormControl>
            <Textarea
              placeholder="Tell us a little bit about..."
              class="resize-none"
              v-bind="componentField"
            />
          </FormControl>
          <FormDescription>
            What is the product description?
          </FormDescription>
          <FormMessage />
        </FormItem>
      </FormField>
      <FormField v-slot="{ value }" name="cost" class="grid gap-2">
        <FormItem v-auto-animate>
          <FormLabel>Cost</FormLabel>
          <NumberField
            class="gap-2"
            :min="0"
            :format-options="{
              style: 'currency',
              currency: 'BRL',
              currencyDisplay: 'code',
              currencySign: 'accounting',
            }"
            :model-value="value"
            @update:model-value="(v) => {
              if (v) {
                setFieldValue('cost', v)
              }
              else {
                setFieldValue('cost', undefined)
              }
            }"
          >
            <NumberFieldContent>
              <NumberFieldDecrement />
              <FormControl>
                <NumberFieldInput />
              </FormControl>
              <NumberFieldIncrement />
            </NumberFieldContent>
          </NumberField>
          <FormDescription>
            What is the product cost?
          </FormDescription>
          <FormMessage />
        </FormItem>
      </FormField>
      <FormField name="type" class="grid gap-2">
        <FormItem class="flex flex-col">
          <FormLabel>Type</FormLabel>
          <Popover>
            <PopoverTrigger as-child>
              <FormControl>
                <Button
                  variant="outline"
                  role="combobox"
                  :class="cn('justify-between', !values.type && 'text-muted-foreground')"
                >
                  {{ values.type ? types.find(
                    (type) => type.value === values.type,
                  )?.label : 'Select type...' }}
                  <CaretSortIcon class="ml-2 h-4 w-4 shrink-0 opacity-50" />
                </Button>
              </FormControl>
            </PopoverTrigger>
            <PopoverContent class="w-[200px] p-0">
              <Command>
                <CommandInput placeholder="Search type..." />
                <CommandEmpty>Nothing found.</CommandEmpty>
                <CommandList>
                  <CommandGroup>
                    <CommandItem
                      v-for="type in types"
                      :key="type.value"
                      :value="type.label"
                      @select="() => {
                        setFieldValue('type', type.value)
                      }"
                    >
                      {{ type.label }}
                      <CheckIcon
                        :class="cn('ml-auto h-4 w-4', type.value === values.type ? 'opacity-100' : 'opacity-0')"
                      />
                    </CommandItem>
                  </CommandGroup>
                </CommandList>
              </Command>
            </PopoverContent>
          </Popover>
          <FormDescription>
            What is the product type?
          </FormDescription>
          <FormMessage />
        </FormItem>
      </FormField>
      <Button type="submit">
        Submit
      </Button>
    </form>
</template>
