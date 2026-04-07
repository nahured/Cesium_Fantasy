
const svg_cache = {};

export async function get_svg_path(name, className) {
    className = className || "icon";

    if (svg_cache[name]) {
        const clone = svg_cache[name].cloneNode(true);
        clone.classList.add(className);
        return clone;
    }

    const svg = await fetch(`./resources/icons/${name}.svg`);
    const text_svg = await svg.text();
    const doom = new DOMParser();
    const svg_doc = doom.parseFromString(text_svg, "image/svg+xml");
    const svg_element = svg_doc.querySelector("svg");

    // 👇 elimina fill hardcodeado del SVG y sus hijos
    svg_element.removeAttribute("fill");
    svg_element.querySelectorAll("[fill]").forEach(el => el.removeAttribute("fill"));
    svg_element.querySelectorAll("[style]").forEach(el => {
        el.style.removeProperty("fill");
        el.style.removeProperty("stroke");
    });
    svg_cache[name] = svg_element;

    const clone = svg_element.cloneNode(true);
    clone.classList.add(className);
    return clone;
}
