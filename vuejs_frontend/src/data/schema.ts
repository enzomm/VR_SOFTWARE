import { z } from 'zod'

export const productSchema = z.object({
  id: z.string(),
  image: z.string(),
  description: z.string(),
  cost: z.string(),  
  type: z.string(),
})

export const newProductSchema = productSchema.omit({ id: true })

export type Product = z.infer<typeof productSchema>
export type NewProduct = z.infer<typeof newProductSchema>
