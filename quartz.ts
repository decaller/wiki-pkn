import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"

const rawDomain = process.env.DOMAIN || process.env.BASE_URL || process.env.QUARTZ_BASE_URL
const cleanDomain = rawDomain ? rawDomain.replace(/^https?:\/\//, "").replace(/\/+$/, "") : undefined

const config = await loadQuartzConfig(cleanDomain ? { baseUrl: cleanDomain } : undefined)
export default config
export const layout = await loadQuartzLayout()

