export interface NavItem {
  title: string
  icon?: string
  children?: NavItem[]
}

export interface NavCollection {
  collection: {
    name: string
    icon?: string
  }
  structure: NavItem[]
}

export type NavStructure = Record<string, NavCollection>

export interface OutlineNavOptions {
  title?: string
  folderDefaultState?: "collapsed" | "open"
  useSavedState?: boolean
}
