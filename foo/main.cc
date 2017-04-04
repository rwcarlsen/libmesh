#include "libmesh/libmesh.h"
#include "libmesh/mesh.h"
#include "libmesh/mesh_generation.h"
#include "libmesh/exodusII_io.h"
#include "libmesh/xdr_io.h"
#include "libmesh/equation_systems.h"
#include "libmesh/elem.h"

using namespace libMesh;

int main (int argc, char** argv)
{
  // Initialize libMesh.
  LibMeshInit init (argc, argv);

  unsigned int n_elem = 750;
  Mesh mesh(init.comm());
  MeshTools::Generation::build_square (mesh,
                                       n_elem, n_elem,
                                       0., 1.,
                                       0., 1.,
                                       QUAD4);

  const unsigned int n_subdomains = 1000;
  const unsigned int n_boundary_ids = 1000;

  unsigned int next_subdomain_id = 0;
  unsigned int next_boundary_id = 0;

  MeshBase::element_iterator       el     = mesh.active_local_elements_begin();
  const MeshBase::element_iterator end_el = mesh.active_local_elements_end();

  for ( ; el != end_el; ++el)
    {
      Elem * elem = *el;

      if(next_subdomain_id < n_subdomains)
      {
        elem->subdomain_id() = next_subdomain_id;
        next_subdomain_id++;
      }

      for(unsigned int side=0; side<elem->n_sides(); side++)
        {
          if(elem->neighbor(side) == NULL)
          {
            if(next_boundary_id < n_boundary_ids)
            {
              mesh.get_boundary_info().add_side(elem, side, next_boundary_id);
              next_boundary_id++;
            }
          }
        }
    }

  mesh.print_info();

  //std::cout << "Started writing xdr file" << std::endl;
  //mesh.write("square.xdr");
  //std::cout << "Finished writing xdr file" << std::endl;

  std::cout << "Started writing exo file" << std::endl;
  mesh.write("/tmp/square.exo");
  std::cout << "Finished writing exo file" << std::endl;

  return 0;
}
