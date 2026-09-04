import { QuartzComponent, QuartzComponentConstructor } from "../quartz/components/types";
export interface OutlineNavOptions {
  title?: string;
  folderDefaultState?: "collapsed" | "open";
  useSavedState?: boolean;
}
declare const OutlineNav: QuartzComponentConstructor<OutlineNavOptions>;
export { OutlineNav };
export default OutlineNav;
